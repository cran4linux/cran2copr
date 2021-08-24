%global __brp_check_rpaths %{nil}
%global packname  sClust
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Toolbox for Unsupervised Spectral Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-class 
Requires:         R-CRAN-cluster 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-class 

%description
Toolbox containing a variety of spectral clustering tools functions. Among
the tools available are the hierarchical spectral clustering algorithm,
the Shi and Malik clustering algorithm, the Perona and Freeman algorithm,
the non-normalized clustering, the Von Luxburg algorithm, the Partition
Around Medoids clustering algorithm, a multi-level clustering algorithm,
recursive clustering and the fast method for all clustering algorithm. As
well as other tools needed to run these algorithms or useful for
unsupervised spectral clustering. This toolbox aims to gather the main
tools for unsupervised spectral classification. See
<http://mawenzi.univ-littoral.fr/> for more information and documentation.

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
