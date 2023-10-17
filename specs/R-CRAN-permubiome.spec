%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  permubiome
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Permutation Based Test for Biomarker Discovery in Microbiome Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dabestr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dabestr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 

%description
The permubiome R package was created to perform a permutation-based
non-parametric analysis on microbiome data for biomarker discovery aims.
This test executes thousands of comparisons in a pairwise manner, after a
random shuffling of data into the different groups of study with a prior
selection of the microbiome features with the largest variation among
groups. Previous to the permutation test itself, data can be normalized
according to different methods proposed to handle microbiome data
('proportions' or 'Anders'). The median-based differences between groups
resulting from the multiple simulations are fitted to a normal
distribution with the aim to calculate their significance. A multiple
testing correction based on Benjamini-Hochberg method (fdr) is finally
applied to extract the differentially presented features between groups of
your dataset. LATEST UPDATES: v1.1 and olders incorporates function to
parse COLUMN format; v1.2 and olders incorporates -optimize- function to
maximize evaluation of features with largest inter-class variation; v1.3
and olders includes the -size.effect- function to perform estimation
statistics using the bootstrap-coupled approach implemented in the
'dabestr' (>=0.3.0) R package. Current v1.3.2 fixed bug with "Class"
recognition and updated 'dabestr' functions.

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
