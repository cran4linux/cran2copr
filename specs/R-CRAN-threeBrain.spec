%global packname  threeBrain
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          3D Brain Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.3.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-htmlwidgets >= 1.3
BuildRequires:    R-CRAN-reticulate >= 1.13
BuildRequires:    R-CRAN-oro.nifti >= 0.9.1
BuildRequires:    R-CRAN-gifti >= 0.7.5
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-startup >= 0.12.0
BuildRequires:    R-CRAN-base64enc >= 0.1.3
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-R6 >= 2.3.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-htmlwidgets >= 1.3
Requires:         R-CRAN-reticulate >= 1.13
Requires:         R-CRAN-oro.nifti >= 0.9.1
Requires:         R-CRAN-gifti >= 0.7.5
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-startup >= 0.12.0
Requires:         R-CRAN-base64enc >= 0.1.3
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-shiny 

%description
In neuroscience, 'AFNI/SUMA' is a great tool to visualize 3D brain.
However, it takes efforts to interact and share the viewer to others. In
addition, 'AFNI/SUMA' doesn't support Windows platform. In the 'EEG/iEEG'
field, it's hard to have multiple cortical electrodes mapped to a template
brain for group analysis. Therefore this package is written aimed at
providing a fast, stable, interactive and easy to share tool based on
'Three.js', a 'WebGL' engine to render 3D objects in the web browser such
that we can display brain surfaces on webpage interactively. This package
translates R objects to JavaScript objects via 'JSON' format, and provides
'R-Shiny' interface to manipulate geometries interactively. The
visualizations can also serve as standalone widgets that can be easily
shared across different platforms. Along with 'rave', another package
developed by Beauchamp's lab at Baylor College Medicine, this package
provides solutions to easily map surface electrodes from multiple subjects
to one template 141 brain.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
