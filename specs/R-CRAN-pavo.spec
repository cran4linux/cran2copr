%global packname  pavo
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Perceptual Analysis, Visualization and Organization of SpectralColour Data in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-magick 
Requires:         R-cluster 
Requires:         R-CRAN-viridisLite 

%description
A cohesive framework for parsing, analyzing and organizing colour from
spectral data.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/testdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
