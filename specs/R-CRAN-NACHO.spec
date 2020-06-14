%global packname  NACHO
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          NanoString Quality Control Dashboard

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-knitr >= 1.25
BuildRequires:    R-CRAN-rmarkdown >= 1.16
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-ggrepel >= 0.8.1
BuildRequires:    R-CRAN-ggbeeswarm >= 0.6.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.9
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-CRAN-rstudioapi >= 0.10
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-knitr >= 1.25
Requires:         R-CRAN-rmarkdown >= 1.16
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-ggrepel >= 0.8.1
Requires:         R-CRAN-ggbeeswarm >= 0.6.0
Requires:         R-CRAN-shinyWidgets >= 0.4.9
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-CRAN-rstudioapi >= 0.10
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-utils 

%description
NanoString nCounter data are gene expression assays where there is no need
for the use of enzymes or amplification protocols and work with
fluorescent barcodes (Geiss et al. (2018) <doi:10.1038/nbt1385>). Each
barcode is assigned a messenger-RNA/micro-RNA (mRNA/miRNA) which after
bonding with its target can be counted. As a result each count of a
specific barcode represents the presence of its target mRNA/miRNA. 'NACHO'
(NAnoString quality Control dasHbOard) is able to analyse the exported
NanoString nCounter data and facilitates the user in performing a quality
control. 'NACHO' does this by visualising quality control metrics,
expression of control genes, principal components and sample specific size
factors in an interactive web application.

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
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
