%global packname  SRS
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Scaling with Ranked Subsampling

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.5.6
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-shinycssloaders >= 1.0.0
BuildRequires:    R-CRAN-shinybusy >= 0.2.2
BuildRequires:    R-CRAN-DT >= 0.16
Requires:         R-CRAN-vegan >= 2.5.6
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-shinycssloaders >= 1.0.0
Requires:         R-CRAN-shinybusy >= 0.2.2
Requires:         R-CRAN-DT >= 0.16

%description
Analysis of species count data in ecology often requires normalization to
an identical sample size. Rarefying (random subsampling without
replacement), which is a popular method for normalization, has been widely
criticized for its poor reproducibility and potential distortion of the
community structure. In the context of microbiome count data, researchers
explicitly advised against the use of rarefying. An alternative to
rarefying is scaling with ranked subsampling (SRS). SRS consists of two
steps. In the first step, the total counts for all OTUs (operational
taxonomic units) or species in each sample are divided by a scaling factor
chosen in such a way that the sum of the scaled counts Cscaled equals
Cmin. In the second step, the non-integer Cscaled values are converted
into integers by an algorithm that we dub ranked subsampling. The Cscaled
value for each OTU or species is split into the integer part Cint (Cint =
floor(Cscaled)) and the fractional part Cfrac (Cfrac = Cscaled - Cints).
Since the sum of Cint is smaller or equal to Cmin, additional delta C =
Cmin - the sum of Cint counts have to be added to the library to reach the
total count of Cmin. This is achieved as follows. OTUs are ranked in the
descending order of their Cfrac values. Beginning with the OTU of the
highest rank, single count per OTU is added to the normalized library
until the total number of added counts reaches delta C and the sum of all
counts in the normalized library equals Cmin. When the lowest Cfrag
involved in picking delta C counts is shared by several OTUs, the OTUs
used for adding a single count to the library are selected in the order of
their Cint values. This selection minimizes the effect of normalization on
the relative frequencies of OTUs. OTUs with identical Cfrag as well as
Cint are sampled randomly without replacement. See Beule & Karlovsky
(2020) <doi:10.7717/peerj.9593> for details.

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
