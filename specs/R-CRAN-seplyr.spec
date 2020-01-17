%global packname  seplyr
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}
Summary:          Improved Standard Evaluation Interfaces for Common DataManipulation Tasks

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 1.9.3
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-wrapr >= 1.9.3
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-CRAN-tidyr 

%description
The 'seplyr' (standard evaluation plying) package supplies improved
standard evaluation adapter methods for important common 'dplyr' data
manipulation tasks. In addition the 'seplyr' package supplies several new
"key operations bound together" methods.  These include
'group_summarize()' (which combines grouping, arranging and calculation in
an atomic unit), 'add_group_summaries()' (which joins grouped summaries
into a 'data.frame' in a well documented manner), 'add_group_indices()'
(which adds per-group identifiers to a 'data.frame' without depending on
row-order), 'partition_mutate_qt()' (which optimizes mutate sequences),
and 'if_else_device()' (which simulates per-row if-else blocks in
expression sequences).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
