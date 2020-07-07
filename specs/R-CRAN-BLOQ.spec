%global packname  BLOQ
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Impute and Analyze Data with BLOQ Observations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-mvtnorm 

%description
It includes estimating the area under the concentrations versus time curve
(AUC) and its standard error for data with Below the Limit of
Quantification (BLOQ) observations. Two approaches are implemented: direct
estimation using censored maximum likelihood, also by first imputing the
BLOQ's using various methods, then compute AUC and its standard error
using imputed data. Technical details can found in Barnett, Helen Yvette,
Helena Geys, Tom Jacobs, and Thomas Jaki. "Methods for Non-Compartmental
Pharmacokinetic Analysis With Observations Below the Limit of
Quantification." Statistics in Biopharmaceutical Research (2020): 1-12.
(available online:
<https://www.tandfonline.com/doi/full/10.1080/19466315.2019.1701546>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/news
%{rlibdir}/%{packname}/INDEX
