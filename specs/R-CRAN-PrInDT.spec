%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PrInDT
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Prediction and Interpretation in Decision Trees for Classification and Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-splitstackshape 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gdata 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-party 
Requires:         R-CRAN-splitstackshape 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-gdata 

%description
Optimization of conditional inference trees from the package 'party' for
classification and regression. For optimization, the model space is
searched for the best tree on the full sample by means of repeated
subsampling. Restrictions are allowed so that only trees are accepted
which do not include pre-specified uninterpretable split results (cf.
Weihs & Buschfeld, 2021a). The function PrInDT() represents the basic
resampling loop for 2-class classification (cf. Weihs & Buschfeld, 2021a).
The function RePrInDT() (repeated PrInDT()) allows for repeated
applications of PrInDT() for different percentages of the observations of
the large and the small classes (cf. Weihs & Buschfeld, 2021c). The
function NesPrInDT() (nested PrInDT()) allows for an extra layer of
subsampling for a specific factor variable (cf. Weihs & Buschfeld, 2021b).
The functions PrInDTMulev() and PrInDTMulab() deal with multilevel and
multilabel classification. In addition to these PrInDT() variants for
classification, the function PrInDTreg() has been developed for regression
problems. Finally, the function PostPrInDT() allows for a posterior
analysis of the distribution of a specified variable in the terminal nodes
of a given tree. In version 2, additionally structured sampling is
implemented in functions PrInDTCstruc() and PrInDTRstruc(). In these
functions, repeated measurements data can be analyzed, too. Moreover,
multilabel 2-stage versions of classification and regression trees are
implemented in functions C2SPrInDT() and R2SPrInDT() as well as
interdependent multilabel models in functions SimCPrInDT() and
SimRPrInDT(). Finally, for mixtures of classification and regression
models functions Mix2SPrInDT() and SimMixPrInDT() are implemented. Most of
these extensions of PrInDT are described in Buschfeld & Weihs (2025Fc).
References: -- Buschfeld, S., Weihs, C. (2025Fc) "Optimizing decision
trees for the analysis of World Englishes and sociolinguistic data",
Cambridge Elements. -- Weihs, C., Buschfeld, S. (2021a) "Combining
Prediction and Interpretation in Decision Trees (PrInDT) - a Linguistic
Example" <doi:10.48550/arXiv.2103.02336>; -- Weihs, C., Buschfeld, S.
(2021b) "NesPrInDT: Nested undersampling in PrInDT"
<doi:10.48550/arXiv.2103.14931>; -- Weihs, C., Buschfeld, S. (2021c)
"Repeated undersampling in PrInDT (RePrInDT): Variation in undersampling
and prediction, and ranking of predictors in ensembles"
<doi:10.48550/arXiv.2108.05129>.

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
