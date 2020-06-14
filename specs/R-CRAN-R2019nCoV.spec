%global packname  R2019nCoV
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Analysis of 2019-nCoV Virus

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pinyin 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pinyin 
Requires:         R-CRAN-maps 

%description
Since December 2019, Wuhan City, Hubei Province has continued to carry out
surveillance of influenza and related diseases, and found multiple cases
of viral pneumonia, all of which were diagnosed with viral pneumonia /
pulmonary infection. On January 12, 2020, the World Health Organization
officially named the new coronavirus causing the pneumonia epidemic in
Wuhan as "2019 New Coronavirus (2019-nCoV)". The current epidemic
situation is very serious, here we developed an R package for 2019-nCoV
analysis(Real-time monitoring and Visualization) by querying real-time
statistics of 2019-nCoV virus cases from
<https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=1580373566110>
and performing follow-up analysis.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
