%global packname  codebook
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Automatic Codebooks from Metadata Encoded in Dataset Attributes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-skimr >= 2.0.0
BuildRequires:    R-CRAN-haven >= 2.0.0
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-forcats >= 0.4.0
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-likert 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-userfriendlyscience 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-skimr >= 2.0.0
Requires:         R-CRAN-haven >= 2.0.0
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-forcats >= 0.4.0
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-likert 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-future 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-userfriendlyscience 

%description
Easily automate the following tasks to describe data frames: Summarise the
distributions, and labelled missings of variables graphically and using
descriptive statistics. For surveys, compute and summarise reliabilities
(internal consistencies, retest, multilevel) for psychological scales.
Combine this information with metadata (such as item labels and labelled
values) that is derived from R attributes. To do so, the package relies on
'rmarkdown' partials, so you can generate HTML, PDF, and Word documents.
Codebooks are also available as tables (CSV, Excel, etc.) and in JSON-LD,
so that search engines can find your data and index the metadata. The
metadata are also available at your fingertips via RStudio Addins.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/_codebook_data_info.Rmd
%doc %{rlibdir}/%{packname}/_codebook_item.Rmd
%doc %{rlibdir}/%{packname}/_codebook_items.Rmd
%doc %{rlibdir}/%{packname}/_codebook_missingness.Rmd
%doc %{rlibdir}/%{packname}/_codebook_scale.Rmd
%doc %{rlibdir}/%{packname}/_codebook_survey_overview.Rmd
%doc %{rlibdir}/%{packname}/_codebook.Rmd
%doc %{rlibdir}/%{packname}/_knit_print_psych.Rmd
%doc %{rlibdir}/%{packname}/_knit_print_scaleDiagnosis.Rmd
%{rlibdir}/%{packname}/_metadata_jsonld.Rmd
%doc %{rlibdir}/%{packname}/_template_codebook.Rmd
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/icon.png
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
