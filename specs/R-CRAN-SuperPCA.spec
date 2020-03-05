%global packname  SuperPCA
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Supervised Principal Component Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matlabr 
BuildRequires:    R-CRAN-spls 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-matlab 
Requires:         R-Matrix 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-glmnet 
Requires:         R-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-timeSeries 
Requires:         R-stats 
Requires:         R-CRAN-matlabr 
Requires:         R-CRAN-spls 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-matlab 

%description
Dimension reduction of complex data with supervision from auxiliary
information. The package contains a series of methods for different data
types (e.g., multi-view or multi-way data) including the supervised
singular value decomposition (SupSVD), supervised sparse and functional
principal component (SupSFPC), supervised integrated factor analysis
(SIFA) and supervised PARAFAC/CANDECOMP factorization (SupCP). When
auxiliary data are available and potentially affect the intrinsic
structure of the data of interest, the methods will accurately recover the
underlying low-rank structure by taking into account the supervision from
the auxiliary data. For more details, see the paper by Gen Li,
<DOI:10.1111/biom.12698>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
