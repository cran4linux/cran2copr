%global packname  nlpred
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimators of Non-Linear Cross-Validated Risks Optimized forSmall Samples

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-cvAUC 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-bde 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-cvAUC 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-bde 
Requires:         R-CRAN-np 
Requires:         R-CRAN-assertthat 

%description
Methods for obtaining improved estimates of non-linear cross-validated
risks are obtained using targeted minimum loss-based estimation,
estimating equations, and one-step estimation (Benkeser, Petersen, van der
Laan (2019), <doi:10.1080/01621459.2019.1668794>). Cross-validated area
under the receiver operating characteristics curve (LeDell, Petersen, van
der Laan (2015), <doi:10.1214/15-EJS1035>) and other metrics are included.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
