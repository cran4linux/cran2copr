%global packname  colordistance
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Distance Metrics for Image Color Similarity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-emdist 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-stats 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-ape 
Requires:         R-mgcv 
Requires:         R-CRAN-emdist 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 

%description
Loads and displays images, selectively masks specified background colors,
bins pixels by color using either data-dependent or automatically
generated color bins, quantitatively measures color similarity among
images using one of several distance metrics for comparing pixel color
clusters, and clusters images by object color similarity. Uses CIELAB,
RGB, or HSV color spaces. Originally written for use with organism
coloration (reef fish color diversity, butterfly mimicry, etc), but easily
applicable for any image set.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
