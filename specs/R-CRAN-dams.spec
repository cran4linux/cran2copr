%global packname  dams
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Dams in the United States from the National Inventory of Dams(NID)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-fauxpas 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-fauxpas 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-readxl 

%description
The single largest source of dams in the United States is the National
Inventory of Dams (NID) <http://nid.usace.army.mil> from the US Army Corps
of Engineers. Entire data from the NID cannot be obtained all at once and
NID's website limits extraction of more than a couple of thousand records
at a time. Moreover, selected data from the NID's user interface cannot
not be saved to a file. In order to make the analysis of this data easier,
all the data from NID was extracted manually. Subsequently, the raw data
was checked for potential errors and cleaned. This package provides sample
cleaned data from the NID and provides functionality to access the entire
cleaned NID data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
