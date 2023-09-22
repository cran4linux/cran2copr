%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chem.databases
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of 3 Chemical Databases from Public Sources

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Contains the Multi-Species Acute Toxicity Database (CAS & SMILES columns
only) [United States (US) Department of Health and Human Services (DHHS)
National Institutes of Health (NIH) National Cancer Institute (NCI),
"Multi-Species Acute Toxicity Database",
<https://cactus.nci.nih.gov/download/acute-toxicity-db/>] combined with
the Toxic Substances Control Act (TSCA) Inventory [United States
Environmental Protection Agency (US EPA), "Toxic Substances Control Act
(TSCA) Chemical Substance Inventory",
<https://www.epa.gov/tsca-inventory/how-access-tsca-inventory} and
<https://cdxapps.epa.gov/oms-substance-registry-services/substance-list-details/169>]
and the Agency for Toxic Substances and Disease Registry (ATSDR) Database
[United States (US) Department of Health and Human Services (DHHS) Centers
for Disease Control and Prevention (CDC)/Agency for Toxic Substances and
Disease Registry (ATSDR), "Agency for Toxic Substances and Disease
Registry (ATSDR) Database",
<https://cdxapps.epa.gov/oms-substance-registry-services/substance-list-details/105>]
in 2 data sets. One data set has a focus on the latter 2 databases and one
data set focuses on the former database. Also contains the collection of
chemical data from Wikipedia compiled in the US EPA CompTox Chemicals
Dashboard [United States Environmental Protection Agency (US EPA) /
Wikimedia Foundation, Inc. "CompTox Chemicals Dashboard v2.2.1",
<https://comptox.epa.gov/dashboard/chemical-lists/WIKIPEDIA>].

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
