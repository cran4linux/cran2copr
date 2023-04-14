%global __brp_check_rpaths %{nil}
%global packname  grImport2
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Importing 'SVG' Graphics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-base64enc 

%description
Functions for importing external vector images and drawing them as part of
'R' plots.  This package is different from the 'grImport' package because,
where that package imports 'PostScript' format images, this package
imports 'SVG' format images.  Furthermore, this package imports a specific
subset of 'SVG', so external images must be preprocessed using a package
like 'rsvg' to produce 'SVG' that this package can import.  'SVG' features
that are not supported by 'R' graphics, e.g., gradient fills, can be
imported and then exported via the 'gridSVG' package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
