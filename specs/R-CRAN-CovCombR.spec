%global __brp_check_rpaths %{nil}
%global packname  CovCombR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Combine Partial Covariance / Relationship Matrices

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-CholWishart 
Requires:         R-Matrix 
Requires:         R-nlme 
Requires:         R-CRAN-CholWishart 

%description
Combine partial covariance matrices using a Wishart-EM algorithm. Methods
are described in the November 2019 article by Akdemir et al.
<https://www.biorxiv.org/content/10.1101/857425v1>. It can be used to
combine partially overlapping covariance matrices from independent trials,
partially overlapping multi-view relationship data from genomic
experiments, partially overlapping Gaussian graphs described by their
covariance structures. High dimensional covariance estimation, multi-view
data integration. high dimensional covariance graph estimation.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
