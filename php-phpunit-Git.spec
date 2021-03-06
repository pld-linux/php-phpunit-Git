%define		pearname	Git
Summary:	Simple wrapper for Git
Name:		php-phpunit-Git
Version:	1.2.0
Release:	1
License:	The BSD 3-Clause License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	25a6254bb2ab12f9f184ba1fd6259a25
URL:		http://pear.phpunit.de/package/Git/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	git-core
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple PHP wrapper for Git.

%prep
%pear_package_setup
mv docs/Git/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE  install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/SebastianBergmann/Git
