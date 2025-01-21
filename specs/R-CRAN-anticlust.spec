%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  anticlust
%global packver   0.8.9-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Subset Partitioning via Anticlustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    glpk-devel
BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-RANN >= 2.6.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-RANN >= 2.6.0
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lpSolve 

%description
The method of anticlustering partitions a pool of elements into groups
(i.e., anticlusters) with the goal of maximizing between-group similarity
or within-group heterogeneity.  The anticlustering approach thereby
reverses the logic of cluster analysis that strives for high within-group
homogeneity and clear separation between groups.  Computationally,
anticlustering is accomplished by maximizing instead of minimizing a
clustering objective function, such as the intra-cluster variance (used in
k-means clustering) or the sum of pairwise distances within clusters. The
main function anticlustering() gives access to optimal and heuristic
anticlustering methods described in Papenberg and Klau (2021;
<doi:10.1037/met0000301>), Brusco et al. (2020; <doi:10.1111/bmsp.12186>),
and Papenberg (2024; <doi:10.1111/bmsp.12315>). The optimal algorithms
require that an integer linear programming solver is installed. This
package will install 'lpSolve'
(<https://cran.r-project.org/package=lpSolve>) as a default solver, but it
is also possible to use the package 'Rglpk'
(<https://cran.r-project.org/package=Rglpk>), which requires the GNU
linear programming kit (<https://www.gnu.org/software/glpk/glpk.html>), or
the package 'Rsymphony' (<https://cran.r-project.org/package=Rsymphony>),
which requires the SYMPHONY ILP solver
(<https://github.com/coin-or/SYMPHONY>). 'Rglpk' and 'Rsymphony' have to
be manually installed by the user because they are only "suggested"
dependencies. Full access to the bicriterion anticlustering method
proposed by Brusco et al. (2020) is given via the function
bicriterion_anticlustering(), while kplus_anticlustering() implements the
full functionality of the k-plus anticlustering approach proposed by
Papenberg (2024). Some other functions are available to solve classical
clustering problems. The function balanced_clustering() applies a cluster
analysis under size constraints, i.e., creates equal-sized clusters. The
function matching() can be used for (unrestricted, bipartite, or
K-partite) matching. The function wce() can be used optimally solve the
(weighted) cluster editing problem, also known as correlation clustering,
clique partitioning problem or transitivity clustering.

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
