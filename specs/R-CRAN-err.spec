%global __brp_check_rpaths %{nil}
%global packname  err
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Customizable Object Sensitive Messages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Messages should provide users with readable information about R objects
without flooding their console. 'cc()' concatenates vector and data frame
values into a grammatically correct string using commas, an ellipsis and
conjunction. 'cn()' allows the user to define a string which varies based
on a count. 'co()' combines the two to produce a customizable object aware
string. The package further facilitates this process by providing five
'sprintf'-like types such as '%n' for the length of an object and '%o' for
its name as well as wrappers for pasting objects and issuing errors,
warnings and messages.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
