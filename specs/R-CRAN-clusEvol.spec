%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clusEvol
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Procedure for Cluster Evolution Analytics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-clusterSim 
Requires:         R-CRAN-dplyr 

%description
Cluster Evolution Analytics allows us to use exploratory what if questions
in the sense that the present information of an object is plugged-in a
dataset in a previous time frame so that we can explore its evolution (and
of its neighbors) to the present. See the URL for the papers associated
with this package, as for instance, Morales-Oñate and Morales-Oñate (2024)
<https://mpra.ub.uni-muenchen.de/120220>.

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
