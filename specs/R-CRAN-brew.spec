%global __brp_check_rpaths %{nil}
%global packname  brew
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Templating Framework for Report Generation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
brew implements a templating framework for mixing text and R code for
report generation. brew template syntax is similar to PHP, Ruby's erb
module, Java Server Pages, and Python's psp module.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/brew-test-1-1.eps
%doc %{rlibdir}/%{packname}/brew-test-1-1.pdf
%doc %{rlibdir}/%{packname}/brew-test-1-2.eps
%doc %{rlibdir}/%{packname}/brew-test-1.aux
%doc %{rlibdir}/%{packname}/brew-test-1.brew
%doc %{rlibdir}/%{packname}/brew-test-1.dvi
%doc %{rlibdir}/%{packname}/brew-test-1.log
%doc %{rlibdir}/%{packname}/brew-test-1.tex
%doc %{rlibdir}/%{packname}/brew-test-2-table.brew
%doc %{rlibdir}/%{packname}/brew-test-2.aux
%doc %{rlibdir}/%{packname}/brew-test-2.brew
%doc %{rlibdir}/%{packname}/brew-test-2.dvi
%doc %{rlibdir}/%{packname}/brew-test-2.html
%doc %{rlibdir}/%{packname}/brew-test-2.log
%doc %{rlibdir}/%{packname}/brew-test-2.tex
%doc %{rlibdir}/%{packname}/brew-test-3.brew
%doc %{rlibdir}/%{packname}/broken.brew
%doc %{rlibdir}/%{packname}/catprint.brew
%doc %{rlibdir}/%{packname}/example1.brew
%doc %{rlibdir}/%{packname}/example2.brew
%doc %{rlibdir}/%{packname}/featurefull.brew
%doc %{rlibdir}/%{packname}/Sweave-test-1-006.eps
%doc %{rlibdir}/%{packname}/Sweave-test-1-006.pdf
%doc %{rlibdir}/%{packname}/Sweave-test-1-007.eps
%doc %{rlibdir}/%{packname}/Sweave-test-1-007.pdf
%doc %{rlibdir}/%{packname}/Sweave-test-1.aux
%doc %{rlibdir}/%{packname}/Sweave-test-1.dvi
%doc %{rlibdir}/%{packname}/Sweave-test-1.log
%doc %{rlibdir}/%{packname}/Sweave-test-1.orig.dvi
%doc %{rlibdir}/%{packname}/Sweave-test-1.tex
%{rlibdir}/%{packname}/INDEX
