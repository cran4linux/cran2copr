%global __brp_check_rpaths %{nil}
%global packname  anticlust
%global packver   0.5.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.6
Release:          1%{?dist}%{?buildtag}
Summary:          Subset Partitioning via Anticlustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-RANN >= 2.6.0
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-RANN >= 2.6.0
Requires:         R-CRAN-Matrix 

%description
The method of anticlustering partitions a pool of elements into groups
(i.e., anticlusters) in such a way that the between-group similarity is
maximized and -- at the same time -- the within-group heterogeneity is
maximized. This reverses the logic of cluster analysis that strives for
high within-group homogeneity and low similarity of the different groups.
Computationally, anticlustering is accomplished by maximizing instead of
minimizing a clustering objective function, such as the intra-cluster
variance (used in k-means clustering) or the sum of pairwise distances
within clusters.  The function anticlustering() implements exact and
heuristic anticlustering algorithms as described in Papenberg and Klau
(2020; <doi:10.1037/met0000301>). The exact approach requires that the GNU
linear programming kit (<https://www.gnu.org/software/glpk/glpk.html>) is
available and the R package 'Rglpk'
(<https://cran.R-project.org/package=Rglpk>) is installed. Some other
functions are available to solve classical clustering problems. The
function balanced_clustering() applies a cluster analysis under size
constraints, i.e., creates equal-sized clusters. The function matching()
can be used for (unrestricted, bipartite, or K-partite) matching. The
function wce() can be used optimally solve the (weighted) cluster editing
problem, also known as correlation clustering, clique partitioning problem
or transitivity clustering.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
