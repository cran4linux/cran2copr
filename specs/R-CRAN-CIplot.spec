%global packname  CIplot
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Functions to Plot Confidence Interval

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-MASS 
Requires:         R-CRAN-multcomp 

%description
Plot confidence interval from the objects of statistical tests such as
t.test(), var.test(), cor.test(), prop.test() and fisher.test() ('htest'
class), Tukey test [TukeyHSD()], Dunnett test [glht() in 'multcomp'
package], logistic regression [glm()], and Tukey or Games-Howell test
[posthocTGH() in 'userfriendlyscience' package]. Users are able to set the
styles of lines and points. This package contains the function to
calculate odds ratios and their confidence intervals from the result of
logistic regression.

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
%{rlibdir}/%{packname}/INDEX
