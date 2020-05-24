%global packname  phonfieldwork
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}
Summary:          Linguistic Phonetic Fieldwork Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-phonTools 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-phonTools 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-rmarkdown 

%description
There are a lot of different typical tasks that have to be solved during
phonetic research and experiments. This includes creating a presentation
that will contain all stimuli, renaming and concatenating multiple sound
files recorded during a session, automatic annotation in 'Praat' TextGrids
(this is one of the sound annotation standards provided by 'Praat'
software, see Boersma & Weenink 2018 <http://www.fon.hum.uva.nl/praat/>),
creating an html table with annotations and spectrograms, and converting
multiple formats ('Praat' TextGrid, 'EXMARaLDA' and 'ELAN'). All of these
tasks can be solved by a mixture of different tools (any programming
language has programs for automatic renaming, and Praat contains scripts
for concatenating and renaming files, etc.). `phonfieldwork` provides a
functionality that will make it easier to solve those tasks independently
of any additional tools. You can also compare the functionality with other
packages: 'rPraat' <https://CRAN.R-project.org/package=rPraat>, 'textgRid'
<https://CRAN.R-project.org/package=textgRid>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
