%global packname  PakPMICS2018
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Multiple Indicator Cluster Survey (MICS) 2017-18 Data forPunjab, Pakistan

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tibble 

%description
Provides data set and function for exploration of Multiple Indicator
Cluster Survey (MICS) 2017-18 data for Punjab, Pakistan. The results of
the present survey are critically important for the purposes of SDG
monitoring, as the survey produces information on 32 global SDG
indicators. The data was collected from 53,840 households selected at the
second stage with systematic random sampling out of a sample of 2,692
clusters selected using Probability Proportional to size sampling. Six
questionnaires were used in the survey: (1) a household questionnaire to
collect basic demographic information on all de jure household members
(usual residents), the household, and the dwelling; (2) a water quality
testing questionnaire administered in three households in each cluster of
the sample; (3) a questionnaire for individual women administered in each
household to all women age 15-49 years; (4) a questionnaire for individual
men administered in every second household to all men age 15-49 years; (5)
an under-5 questionnaire, administered to mothers (or caretakers) of all
children under 5 living in the household; and (6) a questionnaire for
children age 5-17 years, administered to the mother (or caretaker) of one
randomly selected child age 5-17 years living in the household
(<http://www.mics.unicef.org/surveys>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
