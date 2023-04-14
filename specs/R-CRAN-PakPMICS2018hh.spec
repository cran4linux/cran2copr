%global __brp_check_rpaths %{nil}
%global packname  PakPMICS2018hh
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Indicator Cluster Survey (MICS) 2017-18 HouseholdQuestionnaire Data for Punjab, Pakistan

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tibble 

%description
Provides data set and function for exploration of Multiple Indicator
Cluster Survey (MICS) 2017-18 Household questionnaire data for Punjab,
Pakistan. The results of the present survey are critically important for
the purposes of Sustainable Development Goals (SDGs) monitoring, as the
survey produces information on 32 global Sustainable Development Goals
(SDGs) indicators. The data was collected from 53,840 households selected
at the second stage with systematic random sampling out of a sample of
2,692 clusters selected using probability proportional to size sampling.
Six questionnaires were used in the survey: (1) a household questionnaire
to collect basic demographic information on all de jure household members
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
%{rlibdir}/%{packname}
