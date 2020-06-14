%global packname  irrNA
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Coefficients of Interrater Reliability - Generalized forRandomly Incomplete Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-stats 
Requires:         R-CRAN-irr 
Requires:         R-stats 

%description
Provides coefficients of interrater reliability, that are generalized to
cope with randomly incomplete (i.e. unbalanced) datasets without any
imputation of missing values or any (row-wise or column-wise) omissions of
actually available data. Applied to complete (balanced) datasets, these
generalizations yield the same results as the common procedures, namely
the Intraclass Correlation according to McGraw & Wong (1996)
<doi:10.1037/1082-989X.1.1.30> and the Coefficient of Concordance
according to Kendall & Babington Smith (1939)
<doi:10.1214/aoms/1177732186>.

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
