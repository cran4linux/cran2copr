%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rEMM
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extensible Markov Model for Modelling Temporal Relationships Between Clusters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stream 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stream 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-igraph 

%description
Implements TRACDS (Temporal Relationships between Clusters for Data
Streams), a generalization of Extensible Markov Model (EMM). TRACDS adds a
temporal or order model to data stream clustering by superimposing a
dynamically adapting Markov Chain. Also provides an implementation of EMM
(TRACDS on top of tNN data stream clustering). Development of this package
was supported in part by NSF IIS-0948893 and R21HG005912 from the National
Human Genome Research Institute. Hahsler and Dunham (2010)
<doi:10.18637/jss.v035.i05>.

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
