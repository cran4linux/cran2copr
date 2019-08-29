%global packname  flippant
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Dithionite Scramblase Assay Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-wmtsa >= 2.0.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-stringi >= 1.1.2
BuildRequires:    R-CRAN-withr >= 1.0.2
BuildRequires:    R-CRAN-RcppRoll >= 0.2.2
BuildRequires:    R-CRAN-assertive.properties >= 0.0.4
BuildRequires:    R-CRAN-assertive.strings >= 0.0.3
BuildRequires:    R-CRAN-assertive.types >= 0.0.3
BuildRequires:    R-CRAN-assertive.files >= 0.0.2
BuildRequires:    R-CRAN-assertive.numbers >= 0.0.2
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-wmtsa >= 2.0.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-minpack.lm >= 1.2.1
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-stringi >= 1.1.2
Requires:         R-CRAN-withr >= 1.0.2
Requires:         R-CRAN-RcppRoll >= 0.2.2
Requires:         R-CRAN-assertive.properties >= 0.0.4
Requires:         R-CRAN-assertive.strings >= 0.0.3
Requires:         R-CRAN-assertive.types >= 0.0.3
Requires:         R-CRAN-assertive.files >= 0.0.2
Requires:         R-CRAN-assertive.numbers >= 0.0.2
Requires:         R-utils 

%description
The lipid scrambling activity of protein extracts and purified scramblases
is often determined using a fluorescence-based assay involving many manual
steps. flippant offers an integrated solution for the analysis and
publication-grade graphical presentation of dithionite scramblase assays,
as well as a platform for review, dissemination and extension of the
strategies it employs. The package's name derives from a play on the fact
that lipid scrambling is also sometimes referred to as 'flipping'.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
