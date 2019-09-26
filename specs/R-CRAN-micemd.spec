%global packname  micemd
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Multiple Imputation by Chained Equations with Multilevel Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jomo >= 2.6.3
BuildRequires:    R-CRAN-mice >= 2.42
BuildRequires:    R-CRAN-mvmeta >= 0.4.7
BuildRequires:    R-Matrix 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-jomo >= 2.6.3
Requires:         R-CRAN-mice >= 2.42
Requires:         R-CRAN-mvmeta >= 0.4.7
Requires:         R-Matrix 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-abind 

%description
Addons for the 'mice' package to perform multiple imputation using chained
equations with two-level data. Includes imputation methods dedicated to
sporadically and systematically missing values. Imputation of continuous,
binary or count variables are available. Following the recommendations of
Audigier, V. et al (2018) <doi:10.1214/18-STS646>, the choice of the
imputation method for each variable can be facilitated by a default choice
tuned according to the structure of the incomplete dataset. Allows
parallel calculation and overimputation for 'mice'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
