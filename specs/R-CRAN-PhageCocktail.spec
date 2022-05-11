%global __brp_check_rpaths %{nil}
%global packname  PhageCocktail
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Design of the Best Phage Cocktail

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-bipartite 
BuildRequires:    R-CRAN-smerc 
BuildRequires:    R-CRAN-RJSONIO 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-bipartite 
Requires:         R-CRAN-smerc 
Requires:         R-CRAN-RJSONIO 

%description
There are 4 possible methods: "ExhaustiveSearch"; "ExhaustivePhi";
"ClusteringSearch"; and "ClusteringPhi". "ExhaustiveSearch"--> gives you
the best phage cocktail from a phage-bacteria infection network. It checks
different phage cocktail sizes from 1 to 7 and only stops before if it
lyses all bacteria. Other option is when users have decided not to obtain
a phage cocktail size higher than a limit value. "ExhaustivePhi"-->
firstly, it finds Phi out. Phi is a formula indicating the necessary phage
cocktail size. Phi needs nestedness temperature and fill, which are
internally calculated. This function will only look for the best
combination (phage cocktail) with a Phi size. "ClusteringSearch"-->
firstly, an agglomerative hierarchical clustering using Ward's algorithm
is calculated for phages. They will be clustered according to bacteria
lysed by them. PhageCocktail() chooses how many clusters are needed in
order to select 1 phage per cluster. Using the phages selected during the
clustering, it checks different phage cocktail sizes from 1 to 7 and only
stops before if it lyses all bacteria. Other option is when users have
decided not to obtain a phage cocktail size higher than a limit value.
"ClusteringPhi"--> firstly, an agglomerative hierarchical clustering using
Ward's algorithm is calculated for phages. They will be clustered
according to bacteria lysed by them. PhageCocktail() chooses how many
clusters are needed in order to select 1 phage per cluster. Once the
function has one phage per cluster, it calculates Phi. If the number of
clusters is less than Phi number, it will be changed to obtain, as
minimum, this quantity of candidates (phages). Then, it calculates the
best combination of Phi phages using those selected during the clustering
with Ward algorithm. If you use PhageCocktail, please cite it as:
"PhageCocktail: An R Package to Design Phage Cocktails from Experimental
Phage-Bacteria Infection Networks". María Victoria Díaz-Galián, Miguel A.
Vega-Rodríguez, Felipe Molina. Computer Methods and Programs in
Biomedicine, 106865, Elsevier Ireland, Clare, Ireland, 2022, ISSN:
0169-2607.

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
