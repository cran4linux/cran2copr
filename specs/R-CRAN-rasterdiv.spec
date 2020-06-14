%global packname  rasterdiv
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Diversity Indices for Numerical Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-svMisc 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-raster 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-svMisc 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pbmcapply 

%description
Providing functions to calculate indices of diversity on numerical
matrices based on information theory. The rationale behind the package is
described in Rocchini, Marcantonio and Ricotta (2017)
<doi:10.1016/j.ecolind.2016.07.039>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
