%global packname  curvHDR
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Filtering of Flow Cytometry Samples

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-feature 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-ptinpoly 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-KernSmooth 
Requires:         R-CRAN-feature 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-hdrcde 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-ptinpoly 
Requires:         R-CRAN-rgl 
Requires:         R-KernSmooth 

%description
Filtering, also known as gating, of flow cytometry samples using the
curvHDR method, which is described in Naumann, U., Luta, G. and Wand, M.P.
(2010) <DOI:10.1186/1471-2105-11-44>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
