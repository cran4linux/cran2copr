%global packname  recluster
%global packver   2.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9
Release:          1%{?dist}%{?buildtag}
Summary:          Ordination Methods for the Analysis of Beta-Diversity Indices

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-cluster 
Requires:         R-CRAN-plotrix 

%description
The analysis of different aspects of biodiversity requires specific
algorithms. For example, in regionalisation analyses, the high frequency
of ties and zero values in dissimilarity matrices produced by
Beta-diversity turnover produces hierarchical cluster dendrograms whose
topology and bootstrap supports are affected by the order of rows in the
original matrix. Moreover, visualisation of biogeographical
regionalisation can be facilitated by a combination of hierarchical
clustering and multi-dimensional scaling. The recluster package provides
robust techniques to visualise and analyse pattern of biodiversity and to
improve occurrence data for cryptic taxa. Other functions related to
recluster (e.g. the biodecrypt family) are currently available in GitHub
at <https://github.com/leondap/recluster>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
