%global packname  DevTreatRules
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Develop Treatment Rules with Observational Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-DynTxRegime 
BuildRequires:    R-CRAN-modelObj 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-DynTxRegime 
Requires:         R-CRAN-modelObj 

%description
Develop and evaluate treatment rules based on: (1) the standard indirect
approach of split-regression, which fits regressions separately in both
treatment groups and assigns an individual to the treatment option under
which predicted outcome is more desirable; (2) the direct approach of
outcome-weighted-learning proposed by Yingqi Zhao, Donglin Zeng, A. John
Rush, and Michael Kosorok (2012) <doi:10.1080/01621459.2012.695674>; (3)
the direct approach, which we refer to as direct-interactions, proposed by
Shuai Chen, Lu Tian, Tianxi Cai, and Menggang Yu (2017)
<doi:10.1111/biom.12676>. Please see the vignette for a walk-through of
how to start with an observational dataset whose design is understood
scientifically and end up with a treatment rule that is trustworthy
statistically, along with an estimation of rule benefit in an independent
sample.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
