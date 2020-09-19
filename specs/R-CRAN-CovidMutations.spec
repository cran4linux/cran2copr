%global packname  CovidMutations
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Mutation Analysis Toolkit for COVID-19 (Coronavirus Disease 2019)

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-VennDiagram 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-stringr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-VennDiagram 

%description
A feasible framework for mutation analysis and reverse transcription
polymerase chain reaction (RT-PCR) assay evaluation of COVID-19, including
mutation profile visualization, statistics and mutation ratio of each
assay. The mutation ratio is conducive to evaluating the coverage of
RT-PCR assays in large-sized samples. Mercatelli, D. and Giorgi, F. M.
(2020) <doi:10.20944/preprints202004.0529.v1>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
