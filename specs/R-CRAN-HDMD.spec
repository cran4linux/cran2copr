%global packname  HDMD
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Statistical Analysis Tools for High Dimension Molecular Data(HDMD)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-MASS 
Requires:         R-CRAN-psych 
Requires:         R-MASS 

%description
High Dimensional Molecular Data (HDMD) typically have many more variables
or dimensions than observations or replicates (D>>N).  This can cause many
statistical procedures to fail, become intractable, or produce misleading
results.  This package provides several tools to reduce dimensionality and
analyze biological data for meaningful interpretation of results. Factor
Analysis (FA), Principal Components Analysis (PCA) and Discriminant
Analysis (DA) are frequently used multivariate techniques.  However, PCA
methods prcomp and princomp do not reflect the proportion of total
variation of each principal component.  Loadings.variation displays the
relative and cumulative contribution of variation for each component by
accounting for all variability in data. When D>>N, the maximum likelihood
method cannot be applied in FA and the the principal axes method must be
used instead, as in factor.pa of the psych package. The factor.pa.ginv
function in this package further allows for a singular covariance matrix
by applying a general inverse method to estimate factor scores. Moreover,
factor.pa.ginv removes and warns of any variables that are constant, which
would otherwise create an invalid covariance matrix. Promax.only further
allows users to define rotation parameters during factor estimation.
Similar to the Euclidean distance, the Mahalanobis distance estimates the
relationship among groups.  pairwise.mahalanobis computes all such
pairwise Mahalanobis distances among groups and is useful for quantifying
the separation of groups in DA. Genetic sequences are composed of discrete
alphabetic characters, which makes estimates of variability difficult.
MolecularEntropy and MolecularMI calculate the entropy and mutual
information to estimate variability and covariability, respectively, of
DNA or Amino Acid sequences.  Functional grouping of amino acids (Atchley
et al 1999) is also available for entropy and mutual information
estimation.  Mutual information values can be normalized by NMI to account
for the background distribution arising from the stochastic pairing of
independent, random sites. Alternatively, discrete alphabetic sequences
can be transformed into biologically informative metrics to be used in
various multivariate procedures.  FactorTransform converts amino acid
sequences using the amino acid indices determined by Atchley et al 2005.

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
