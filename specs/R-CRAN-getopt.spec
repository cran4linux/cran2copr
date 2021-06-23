%global __brp_check_rpaths %{nil}
%global packname  getopt
%global packver   1.20.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.20.3
Release:          4%{?dist}%{?buildtag}
Summary:          C-Like 'getopt' Behavior

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Package designed to be used with Rscript to write ``#!'' shebang scripts
that accept short and long flags/options. Many users will prefer using
instead the packages optparse or argparse which add extra features like
automatically generated help option and usage, support for default values,
positional argument support, etc.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@/path/to/Rscript@/usr/bin/Rscript@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
