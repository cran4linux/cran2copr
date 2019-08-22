%global packname  apparent
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Accurate Parentage Analysis in the Absence of GuidingInformation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-outliers 
Requires:         R-CRAN-outliers 

%description
Performs parentage analysis based on a test of genetic identity between
expected progeny (EPij), built using Single Nucleotide Polymorphism (SNP)
homozygous loci from all pairs of possible parents (i and j), and all
potential offspring (POk). Using the Gower Dissimilarity metric (GD),
genetic identity between EPij and POk is taken as evidence that
individuals i and j are the true parents of offspring k.  Evaluation of
triad (two parents + offspring) significance is based on the distribution
of all GD (EPij|k) values. Specifically, a Dixon test is used to identify
a gap-based threshold that separates true triads and from spurious
associations. For any offspring not successfully assigned to a pair of
parents, perhaps due to the absence of one parent from the test
population, a non-mandatory Dyad analysis can be employed to identify a
likely single parent for a given offspring. In this analysis, a two-stage
test is applied to discriminate an offspring's true parent from its other
close relatives (e.g. siblings) that may also be present in the
population. In the first stage, 'apparent' calculates the mean GD (GDM)
between a POk and all expected progeny arising from the j possible triads
involving potential parent i. In the second stage, it calculates a
coefficient of variation (GDCV) among the pairwise GD's between POk and
each expected progeny arising from the j triads involving potential parent
i. An individual that is simultaneously a low outlier in the first test
and a high outlier in the second is identified as a likely parent of POk.
In an effort to facilitate interpretation, results of both the triad and
optional dyad analyses are presented in tabular and graphical form.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
