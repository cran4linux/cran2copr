%global __brp_check_rpaths %{nil}
%global packname  seg
%global packver   0.5-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          3%{?dist}%{?buildtag}
Summary:          Measuring Spatial Segregation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-splancs 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-splancs 

%description
Measuring spatial segregation. The methods implemented in this package
include White's P index (1983) <doi:10.1086/227768>, Morrill's D(adj)
(1991), Wong's D(w) and D(s) (1993) <doi:10.1080/00420989320080551>, and
Reardon and O'Sullivan's set of spatial segregation measures (2004)
<doi:10.1111/j.0081-1750.2004.00150.x>.

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
%{rlibdir}/%{packname}/libs
