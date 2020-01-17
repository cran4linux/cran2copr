%global packname  TITAN2
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Threshold Indicator Taxa Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-snow 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-snow 

%description
Uses indicator species scores across binary partitions of a sample set to
detect congruence in taxon-specific changes of abundance and occurrence
frequency along an environmental gradient as evidence of an ecological
community threshold.  Relevant references include: Baker, ME and RS King.
2010. A new method for detecting and interpreting biodiversity and
ecological community thresholds.  Methods in Ecology and Evolution 1(1):
25:37. King, RS and ME Baker. 2010. Considerations for identifying and
interpreting ecological community thresholds.  Journal of the North
American Benthological Association 29(3):998-1008. Baker ME and RS King.
2013. Of TITAN and straw men: an appeal for greater understanding of
community data. Freshwater Science 32(2):489-506.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
