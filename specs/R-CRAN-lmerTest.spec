%global packname  lmerTest
%global packver   3.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          3%{?dist}
Summary:          Tests in Linear Mixed Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.10
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 >= 1.1.10
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 

%description
Provides p-values in type I, II or III anova and summary tables for lmer
model fits (cf. lme4) via Satterthwaite's degrees of freedom method. A
Kenward-Roger method is also available via the pbkrtest package. Model
selection methods include step, drop1 and anova-like tables for random
effects (ranova). Methods for Least-Square means (LS-means) and tests of
linear contrasts of fixed effects are also available.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
