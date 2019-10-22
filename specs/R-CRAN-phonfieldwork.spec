%global packname  phonfieldwork
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
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
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-phonTools 
Requires:         R-grDevices 
Requires:         R-CRAN-DT 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-rmarkdown 

%description
There are a lot of different typical tasks that should be solved during
phonetic research and experiments, such as creation of presentation that
will contain all stimuli, rename and concatenate multiple sound files
recorded during phonetic session, automatically annotate 'Praat' TextGrids
(this is one of the sound annotation standards provided by 'Praat'
software, see Paul Boersma, David Weenink 2018
<http://www.fon.hum.uva.nl/praat/>), create an html that includes
annotation and spectrogram tables, convert multiple formats ('Praat'
TextGrid, 'EXMARaLDA' and 'ELAN') into each other. All those tasks could
be solved by mixture of different tools (some programs in any programming
language for automatic renaming, some Praat scripts for the file
concatenation and renaming, etc). This package provides functionality that
will make it easier to solve those tasks independently of any of tools.
You could also compare the functionality with other packages: 'rPraat'
<https://CRAN.R-project.org/package=rPraat>, 'textgRid'
<https://CRAN.R-project.org/package=textgRid>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
