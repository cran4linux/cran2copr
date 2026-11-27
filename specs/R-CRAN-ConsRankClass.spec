%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ConsRankClass
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classification and Clustering of Preference Rankings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ConsRank >= 3.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ConsRank >= 3.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-janitor 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-gtools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-lattice 
Requires:         R-stats 
Requires:         R-utils 

%description
Tree-based classification and soft-clustering method for preference
rankings, with tools for external validation of fuzzy clustering, and
Kemeny-equivalent augmented unfolding. It contains the recursive
partitioning algorithm for preference rankings, non-parametric tree-based
method for a matrix of preference rankings as a response variable. It
contains also the distribution-free soft clustering method for preference
rankings, namely the K-median cluster component analysis (CCA). The
package depends on the 'ConsRank' R package. Options for validate the
tree-based method are both test-set procedure and V-fold cross validation,
with the s-SE rule. In the trees, the class of a node can be computed with
the BOLT algorithm and constrained to a given number of buckets, to a
given pattern of bucket sizes or to a top-k list; the impurity can be the
pairwise impurity of D'Ambrosio and Heiser (2016) or the distance of the
judges from the class of the node (median impurity), and the objects not
ranked by the judges can be tied in the last position or treated as
unknown. Descriptive tools: marginal and pairs matrices, projection of the
rankings on the permutation polytope, clustering of the objects,
multidimensional scaling of the judges, each with its plot (base graphics
or 'lattice'). The package contains the routines to compute the adjusted
concordance index (a fuzzy version of the adjusted rand index) and the
normalized degree of concordance (the corresponding fuzzy version of the
rand index). The package also contains routines to perform the
Kemeny-equivalent augmented unfolding. The MDS engine is either the
function 'smacofSym' from the package 'smacof' or the function mdscale()
of this package, metric and non-metric multidimensional scaling with the
criteria of the 'MATLAB' function of the same name (stress, sstress,
metric stress, metric sstress, Sammon mapping, strain). It also contains
distances between complete rankings (Kendall, Cayley, Hamming, Ulam,
Spearman footrule, Spearman), the Mallows (distance-based) model for any
of these distances, with exact normalising constants, maximum likelihood
estimation and exact simulation, mixtures of distance-based models fitted
by the EM algorithm with model selection by BIC and ICL, and
distance-based tree models in which a Mallows model is fitted within each
node (also for top-k partial rankings). Essential references: D'Ambrosio,
A., Vera, J.F., and Heiser, W.J. (2021)
<doi:10.1080/00273171.2021.1899892>; D'Ambrosio, A., Amodio, S., Iorio,
C., Pandolfo, G., and Siciliano, R. (2021)
<doi:10.1007/s00357-020-09367-0>; D'Ambrosio, A., and Heiser, W.J. (2019)
<doi:10.1007/s41237-018-0069-5>; D'Ambrosio, A., and Heiser W.J. (2016)
<doi:10.1007/s11336-016-9505-1>; Hullermeier, E., Rifqi, M., Henzgen, S.,
and Senge, R. (2012) <doi:10.1109/TFUZZ.2011.2179303>; Murphy, T.B., and
Martin, D. (2003) <doi:10.1016/S0167-9473(02)00165-2>; Lee, P.H., and Yu,
P.L.H. (2010) <doi:10.1016/j.csda.2010.01.027>; Marden, J.I. (1995)
<ISBN:0412995212>.

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
