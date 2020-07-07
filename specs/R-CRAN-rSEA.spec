%global packname  rSEA
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}
Summary:          Simultaneous Enrichment Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-hommel >= 1.4
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-hommel >= 1.4
Requires:         R-CRAN-ggplot2 

%description
SEA performs simultaneous feature-set testing for (gen)omics data. It
tests the unified null hypothesis controls the family-wise error rate for
all possible pathways. The unified null hypothesis is defined as: "The
proportion of true features in the set is less than or equal to the
threshold c", where c is selected by the user. Family-wise error rate
control is provided through use of closed testing with Simes test. For
more information on closed testing with Simes see Goeman et al. (2019)
<doi:10.1093/biomet/asz041> and for more information about the properties
and performance of SEA procedure see Ebrahimpoor et al. (2019)
<doi:10.1093/bib/bbz074>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
