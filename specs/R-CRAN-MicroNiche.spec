%global __brp_check_rpaths %{nil}
%global packname  MicroNiche
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Microbial Niche Measurements

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 

%description
Measures niche breadth and overlap of microbial taxa from large matrices.
Niche breadth measurements include Levins' niche breadth (Bn) index,
Hurlbert's Bn and Feinsinger's proportional similarity (PS) index.
(Feinsinger, P., Spears, E.E., Poole, R.W. (1981) <doi:10.2307/1936664>).
Niche overlap measurements include Levin's Overlap (Ludwig, J.A. and
Reynolds, J.F. (1988, ISBN:0471832359)) and a Jaccard similarity index of
Feinsinger's PS values between taxa pairs, as Proportional Overlap.

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
