%global packname  tangles
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          2%{?dist}
Summary:          Anonymization of Spatial Point Patterns and Raster Objects

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-sp 

%description
Spatial data anonymization preserves confidentiality. Using methods
described in Zandbergen (2014) <doi:10.1155/2014/567049>, spatial data
anonymization is achieved by dithering original spatial coordinates with
combinations of randomized vertical, horizontal and rotational shifts.
This can apply to non-grid spatial point patterns and raster objects, and
the methods preserve the same spatial characteristics and relationships of
the original data. Unique hash keying enables data subjected to
anonymization sequences to be re-identified where required.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
