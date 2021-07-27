%global __brp_check_rpaths %{nil}
%global packname  SOMEnv
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          SOM Algorithm for the Analysis of Multivariate Environmental Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinycustomloader 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-openair 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinycustomloader 

%description
Analysis of multivariate environmental high frequency data by
Self-Organizing Map and k-means clustering algorithms. By means of the
graphical user interface it provides a comfortable way to elaborate by
self-organizing map algorithm rather big datasets (txt files up to 100 MB
) obtained by environmental high-frequency monitoring by
sensors/instruments. The functions present in the package are based on
'kohonen' and 'openair' packages implemented by functions embedding
Vesanto et al. (2001)
<http://www.cis.hut.fi/projects/somtoolbox/package/papers/techrep.pdf>
heuristic rules for map initialization parameters, k-means clustering
algorithm and map features visualization. Cluster profiles visualization
as well as graphs dedicated to the visualization of time-dependent
variables Licen et al. (2020) <doi:10.4209/aaqr.2019.08.0414> are
provided.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
