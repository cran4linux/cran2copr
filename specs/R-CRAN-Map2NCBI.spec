%global packname  Map2NCBI
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Mapping Markers to the Nearest Genomic Feature

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rentrez >= 1.2
Requires:         R-CRAN-rentrez >= 1.2

%description
Allows the user to generate a list of features (gene, pseudo, RNA, CDS,
and/or UTR) directly from NCBI database for any species with a current
build available. Option to save downloaded and formatted files is
available, and the user can prioritize the feature list based on type and
assembly builds present in the current build used. The user can then use
the list of features generated or provide a list to map a set of markers
(designed for SNP markers with a single base pair position available) to
the closest feature based on the map build. This function does require map
positions of the markers to be provided and the positions should be based
on the build being queried through NCBI.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
