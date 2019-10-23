%global packname  GWLelast
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Geographically Weighted Logistic Elastic Net Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spgwr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spgwr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-stats 

%description
Fit a geographically weighted logistic elastic net regression. Detailed
explanations can be found in Yoneoka et al. (2016): New algorithm for
constructing area-based index with geographical heterogeneities and
variable selection: An application to gastric cancer screening
<doi:10.1038/srep26582>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
