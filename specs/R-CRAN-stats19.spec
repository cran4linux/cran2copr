%global packname  stats19
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Work with Open Road Traffic Casualty Data from Great Britain

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readr 

%description
Tools to help download, process and analyse the UK road collision data
collected using the 'STATS19' form. The data are provided as 'CSV' files
with detailed road safety data about the circumstances of car crashes and
other incidents on the roads resulting in casualties in Great Britain from
1979, the types (including make and model) of vehicles involved and the
consequential casualties.  The statistics relate only to personal
casualties on public roads that are reported to the police, and
subsequently recorded, using the 'STATS19' accident reporting form. See
the Department for Transport website
<https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data>
for more information on these data.

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
%doc %{rlibdir}/%{packname}/2day-slides.Rmd
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ggtheme-plot.png
%doc %{rlibdir}/%{packname}/iow_example.R
%{rlibdir}/%{packname}/national-cycling-data.R
%doc %{rlibdir}/%{packname}/rstudio-autocomplete.png
%doc %{rlibdir}/%{packname}/stats-19-exercises.Rmd
%doc %{rlibdir}/%{packname}/tmap-zones-interactive.png
%doc %{rlibdir}/%{packname}/ts_example.R
%doc %{rlibdir}/%{packname}/walking-cycling-innovations-slides.Rmd
%{rlibdir}/%{packname}/INDEX
