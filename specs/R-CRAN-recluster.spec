%global packname  recluster
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          2%{?dist}
Summary:          Ordination Methods for the Analysis of Beta-Diversity Indices

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-cluster 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-cluster 

%description
Beta-diversity indices provide dissimilarity matrices with particular
distribution of data requiring specific treatment. For example the high
frequency of ties and zero values in turnover indices produces
hierarchical cluster dendrograms whose topology and bootstrap supports are
affected by the order of rows in the original matrix. Moreover,
biogeographical regionalization can be facilitated by a combination of
hierarchical clustering and multi-dimensional scaling. The recluster
package provides robust techniques to analyze pattern of similarity in
species composition.

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

%files
%{rlibdir}/%{packname}
